
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DoubleLayerModelModule import DoubleLayerModel







class TrasattiBuzzancaModel(DoubleLayerModel):
    """
    Class representing the `TrasattiBuzzancaModel` entity, which inherits from:
    - DoubleLayerModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f57a7dac_2ec2_4d51_b697_01a844c4467f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TrasattiBuzzancaModel'`
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
    obj = TrasattiBuzzancaModel(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f57a7dac_2ec2_4d51_b697_01a844c4467f',
    
    class_name='TrasattiBuzzancaModel',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f57a7dac_2ec2_4d51_b697_01a844c4467f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TrasattiBuzzancaModel',
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
    

    
    

    

    