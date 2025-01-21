
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .ElectricCurrentDensityUnitModule import ElectricCurrentDensityUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .MeasurementUnitModule import MeasurementUnit



from .PrefixedUnitModule import PrefixedUnit








class StatamperePerSquareCentiMetre(ElectricCurrentDensityUnit, SINonCoherentUnit, MeasurementUnit, PrefixedUnit):
    """
    Class representing the `StatamperePerSquareCentiMetre` entity, which inherits from:
    - ElectricCurrentDensityUnit, SINonCoherentUnit, MeasurementUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#StatamperePerSquareCentiMetre'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StatamperePerSquareCentiMetre'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StatamperePerSquareCentiMetre(
    
    class_iri='https://w3id.org/emmo#StatamperePerSquareCentiMetre',
    
    class_name='StatamperePerSquareCentiMetre',
    
    hasSIConversionMultiplier="example_value",
    
    elucidation="example_value",
    
    qudtReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    unitSymbol="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#StatamperePerSquareCentiMetre',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'StatamperePerSquareCentiMetre',
        
        alias="class_name"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    


    
    

    

    