
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .NonSIUnitModule import NonSIUnit



from .PerThermalTransmittanceUnitModule import PerThermalTransmittanceUnit



from .MeasurementUnitModule import MeasurementUnit








class M2_Hr_Deg_C_Per_KiloCal_It(NonSIUnit, PerThermalTransmittanceUnit, MeasurementUnit):
    """
    Class representing the `M2_Hr_Deg_C_Per_KiloCal_It` entity, which inherits from:
    - NonSIUnit, PerThermalTransmittanceUnit, MeasurementUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#M2_Hr_Deg_C_Per_KiloCal_It'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'M2_Hr_Deg_C_Per_KiloCal_It'`
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
    obj = M2_Hr_Deg_C_Per_KiloCal_It(
    
    class_iri='https://w3id.org/emmo#M2_Hr_Deg_C_Per_KiloCal_It',
    
    class_name='M2_Hr_Deg_C_Per_KiloCal_It',
    
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
        
            'https://w3id.org/emmo#M2_Hr_Deg_C_Per_KiloCal_It',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'M2_Hr_Deg_C_Per_KiloCal_It',
        
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
    


    
    

    

    