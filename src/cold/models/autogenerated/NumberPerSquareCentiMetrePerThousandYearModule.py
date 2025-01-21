
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .NonSIUnitModule import NonSIUnit



from .PerLengthTimeUnitModule import PerLengthTimeUnit



from .MeasurementUnitModule import MeasurementUnit



from .PrefixedUnitModule import PrefixedUnit








class NumberPerSquareCentiMetrePerThousandYear(NonSIUnit, PerLengthTimeUnit, MeasurementUnit, PrefixedUnit):
    """
    Class representing the `NumberPerSquareCentiMetrePerThousandYear` entity, which inherits from:
    - NonSIUnit, PerLengthTimeUnit, MeasurementUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#NumberPerSquareCentiMetrePerThousandYear'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NumberPerSquareCentiMetrePerThousandYear'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
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
    obj = NumberPerSquareCentiMetrePerThousandYear(
    
    class_iri='https://w3id.org/emmo#NumberPerSquareCentiMetrePerThousandYear',
    
    class_name='NumberPerSquareCentiMetrePerThousandYear',
    
    hasSIConversionMultiplier="example_value",
    
    qudtReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    unitSymbol="example_value",
    
    ucumCode="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#NumberPerSquareCentiMetrePerThousandYear',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'NumberPerSquareCentiMetrePerThousandYear',
        
        alias="class_name"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
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
    


    
    

    

    