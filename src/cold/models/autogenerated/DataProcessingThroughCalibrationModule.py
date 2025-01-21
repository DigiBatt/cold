
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from ..custom.LinkedDataModelModule import LinkedDataModel







class DataProcessingThroughCalibration(LinkedDataModel):
    """
    Class representing the `DataProcessingThroughCalibration` entity, which inherits from:
    - LinkedDataModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DataProcessingThroughCalibration'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DataProcessingThroughCalibration'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DataProcessingThroughCalibration(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#DataProcessingThroughCalibration',
    
    class_name='DataProcessingThroughCalibration',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DataProcessingThroughCalibration',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DataProcessingThroughCalibration',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    