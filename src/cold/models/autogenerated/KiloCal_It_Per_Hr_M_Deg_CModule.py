
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .ThermalConductivityUnitModule import ThermalConductivityUnit



from .NonSIUnitModule import NonSIUnit



from .KiloPrefixedUnitModule import KiloPrefixedUnit



from .PrefixedUnitModule import PrefixedUnit








class KiloCal_It_Per_Hr_M_Deg_C(ThermalConductivityUnit, NonSIUnit, KiloPrefixedUnit, PrefixedUnit):
    """
    Class representing the `KiloCal_It_Per_Hr_M_Deg_C` entity, which inherits from:
    - ThermalConductivityUnit, NonSIUnit, KiloPrefixedUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#KiloCal_It_Per_Hr_M_Deg_C'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KiloCal_It_Per_Hr_M_Deg_C'`
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
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = KiloCal_It_Per_Hr_M_Deg_C(
    
    class_iri='https://w3id.org/emmo#KiloCal_It_Per_Hr_M_Deg_C',
    
    class_name='KiloCal_It_Per_Hr_M_Deg_C',
    
    hasSIConversionMultiplier="example_value",
    
    elucidation="example_value",
    
    qudtReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    unitSymbol="example_value",
    
    ucumCode="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#KiloCal_It_Per_Hr_M_Deg_C',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'KiloCal_It_Per_Hr_M_Deg_C',
        
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
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    


    
    

    

    