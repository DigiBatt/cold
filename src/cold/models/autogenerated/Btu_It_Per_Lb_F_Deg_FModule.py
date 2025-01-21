
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .NonSIUnitModule import NonSIUnit



from .EntropyPerMassUnitModule import EntropyPerMassUnit



from .MeasurementUnitModule import MeasurementUnit








class Btu_It_Per_Lb_F_Deg_F(NonSIUnit, EntropyPerMassUnit, MeasurementUnit):
    """
    Class representing the `Btu_It_Per_Lb_F_Deg_F` entity, which inherits from:
    - NonSIUnit, EntropyPerMassUnit, MeasurementUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#Btu_It_Per_Lb_F_Deg_F'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Btu_It_Per_Lb_F_Deg_F'`
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
    obj = Btu_It_Per_Lb_F_Deg_F(
    
    class_iri='https://w3id.org/emmo#Btu_It_Per_Lb_F_Deg_F',
    
    class_name='Btu_It_Per_Lb_F_Deg_F',
    
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
        
            'https://w3id.org/emmo#Btu_It_Per_Lb_F_Deg_F',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'Btu_It_Per_Lb_F_Deg_F',
        
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
    


    
    

    

    