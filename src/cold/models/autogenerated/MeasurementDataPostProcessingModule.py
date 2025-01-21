
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from ..custom.LinkedDataModelModule import LinkedDataModel







class MeasurementDataPostProcessing(LinkedDataModel):
    """
    Class representing the `MeasurementDataPostProcessing` entity, which inherits from:
    - LinkedDataModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#MeasurementDataPostProcessing'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MeasurementDataPostProcessing'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MeasurementDataPostProcessing(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#MeasurementDataPostProcessing',
    
    class_name='MeasurementDataPostProcessing',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#MeasurementDataPostProcessing',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MeasurementDataPostProcessing',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    