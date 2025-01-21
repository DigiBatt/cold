
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ProductionEngineeringModule import ProductionEngineering



from .MaterialsProcessingModule import MaterialsProcessing







class MaterialSynthesis(ProductionEngineering, MaterialsProcessing):
    """
    Class representing the `MaterialSynthesis` entity, which inherits from:
    - ProductionEngineering, MaterialsProcessing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fa9cfc5d_9c3c_4856_a708_28be3858917e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaterialSynthesis'`
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
    obj = MaterialSynthesis(
    
    class_iri='https://w3id.org/emmo#EMMO_fa9cfc5d_9c3c_4856_a708_28be3858917e',
    
    class_name='MaterialSynthesis',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fa9cfc5d_9c3c_4856_a708_28be3858917e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaterialSynthesis',
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
    

    
    

    

    