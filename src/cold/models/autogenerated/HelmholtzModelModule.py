
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DoubleLayerModelModule import DoubleLayerModel







class HelmholtzModel(DoubleLayerModel):
    """
    Class representing the `HelmholtzModel` entity, which inherits from:
    - DoubleLayerModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9bc02662_9799_4593_906d_638a841d7352'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HelmholtzModel'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HelmholtzModel(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9bc02662_9799_4593_906d_638a841d7352',
    
    class_name='HelmholtzModel',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9bc02662_9799_4593_906d_638a841d7352',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HelmholtzModel',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    