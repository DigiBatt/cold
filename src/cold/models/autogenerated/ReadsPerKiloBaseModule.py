
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .DerivedUnitModule import DerivedUnit



from .NonSIUnitModule import NonSIUnit



from .NonPrefixedUnitModule import NonPrefixedUnit



from .FractionUnitModule import FractionUnit








class ReadsPerKiloBase(DerivedUnit, NonSIUnit, NonPrefixedUnit, FractionUnit):
    """
    Class representing the `ReadsPerKiloBase` entity, which inherits from:
    - DerivedUnit, NonSIUnit, NonPrefixedUnit, FractionUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#ReadsPerKiloBase'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ReadsPerKiloBase'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ReadsPerKiloBase(
    
    class_iri='https://w3id.org/emmo#ReadsPerKiloBase',
    
    class_name='ReadsPerKiloBase',
    
    elucidation="example_value",
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#ReadsPerKiloBase',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'ReadsPerKiloBase',
        
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    


    
    

    

    