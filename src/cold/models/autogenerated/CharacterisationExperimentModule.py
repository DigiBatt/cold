
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ExperimentModule import Experiment







class CharacterisationExperiment(Experiment):
    """
    Class representing the `CharacterisationExperiment` entity, which inherits from:
    - Experiment

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationExperiment'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CharacterisationExperiment'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CharacterisationExperiment(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationExperiment',
    
    class_name='CharacterisationExperiment',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationExperiment',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CharacterisationExperiment',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    